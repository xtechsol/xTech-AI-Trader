import torch
from torch import nn
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from data_collector import DataCollector

class TradingModel(nn.Module):
    def __init__(self, input_dim, hidden_dim, output_dim):
        super(TradingModel, self).__init__()
        self.layer1 = nn.Linear(input_dim, hidden_dim)
        self.layer2 = nn.Linear(hidden_dim, hidden_dim)
        self.layer3 = nn.Linear(hidden_dim, output_dim)
        self.relu = nn.ReLU()

    def forward(self, x):
        x = self.relu(self.layer1(x))
        x = self.relu(self.layer2(x))
        x = self.layer3(x)
        return x

class AIModel:
    def __init__(self, data_collector):
        self.data_collector = data_collector
        self.model = None
        self.scaler = StandardScaler()

    def prepare_data(self, market_data, sentiment):
        features = market_data[['Open', 'High', 'Low', 'Close', 'Volume']].values
        features = self.scaler.fit_transform(features)
        sentiment_array = np.full((features.shape[0], 1), sentiment)
        X = np.hstack((features, sentiment_array))
        y = (market_data['Close'].shift(-1) > market_data['Close']).astype(int).values[:-1]  # Predict if price will go up
        return train_test_split(X, y, test_size=0.2, random_state=42)

    def train_model(self, X_train, X_test, y_train, y_test):
        input_dim = X_train.shape[1]
        output_dim = 2  # Buy or Sell

        self.model = TradingModel(input_dim, 64, output_dim)
        criterion = nn.CrossEntropyLoss()
        optimizer = torch.optim.Adam(self.model.parameters(), lr=0.01)

        X_train_tensor = torch.FloatTensor(X_train)
        y_train_tensor = torch.LongTensor(y_train)

        for epoch in range(100):
            self.model.train()
            optimizer.zero_grad()
            outputs = self.model(X_train_tensor)
            loss = criterion(outputs, y_train_tensor)
            loss.backward()
            optimizer.step()

            if (epoch + 1) % 10 == 0:
                print(f'Epoch [{epoch + 1}/100], Loss: {loss.item():.4f}')

        # Test accuracy
        self.model.eval()
        with torch.no_grad():
            X_test_tensor = torch.FloatTensor(X_test)
            y_test_tensor = torch.LongTensor(y_test)
            outputs = self.model(X_test_tensor)
            _, predicted = torch.max(outputs.data, 1)
            accuracy = (predicted == y_test_tensor).sum().item() / len(y_test)
            print(f'Test Accuracy: {accuracy:.2f}')

    def predict(self, features):
        if self.model is None:
            raise ValueError("Model has not been trained yet.")
        self.model.eval()
        with torch.no_grad():
            features_tensor = torch.FloatTensor(features.reshape(1, -1))
            outputs = self.model(features_tensor)
            _, predicted = torch.max(outputs, 1)
            return "buy" if predicted.item() == 1 else "sell"

if __name__ == "__main__":
    collector = DataCollector(load_config())
    ai = AIModel(collector)
    market_data, sentiment = collector.collect_data(['BTC-USD'])
    X_train, X_test, y_train, y_test = ai.prepare_data(market_data, sentiment)
    ai.train_model(X_train, X_test, y_train, y_test)
    prediction = ai.predict(X_test[0])
    print("Prediction:", prediction)
