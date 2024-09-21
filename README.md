# 📊 Simple CRM System 



I developed a **Simple CRM System** with **Streamlit** to record and manage sales. The system allows users to easily input essential sales information such as:

- 📨 Seller's email
- 📅 Date and time of sale
- 💰 Sale value
- 📦 Quantity of products sold
- 🛍️ Product sold


## Technologies used

- 🖥️ **Frontend**: Built with **Streamlit**.
- 🛠️ **Backend**: **PostgreSQL** database, validated with **Pydantic** and integrated via **SQLAlchemy**.
- 📦 **Docker Environment**: The entire application runs inside **Docker** containers, ensuring consistency and easy deployment.



## 🌟 Features

- 🧾 **Comprehensive Sales Registration**: Includes details such as seller's email, amount, date, and product.
- 💾 **Database Integration**: All records are efficiently stored in a local **PostgreSQL** database.
- 🛡️ **Data Validation**: Using **Pydantic** ensures that all entered data is correct and within expected parameters.
- 📊 **Simple and Intuitive Interface**: The **Streamlit** frontend provides a smooth and functional user experience.
- 📖 **Documentation**: Created using **MkDocs** and served locally through Docker.


## 🚀 Quick Start

This project is super easy to get up and running! All you need is Docker.


### Prerequisites
- Docker installed on your machine

### Installation and Setup

1. To install **Docker** on your machine you can follow [this steps](https://docs.docker.com/engine/install/ubuntu/#install-using-the-repository).

2. Clone the repository to your local machine:

```bash
git clone https://github.com/kefrankk/CRM-system-and-sales.git
  ```

3. Navigate to the project directory:

```bash
cd CRM-system-and-sales
```

4. Start Git repository:

```bash
git init
```

3. Run the Docker setup:

```bash
sudo docker-compose up --build
```

4. Access the application: Once Docker sets up the environment, you can access the app at:

- CRM System: `http://localhost:8501`
- Documentation (MkDocs): `http://localhost:8000`

### Environment Variables
To manage your database credentials, make sure to set up a `.env` file in the project directory with your desired credentials:

```bash
DB_HOST = localhost
DB_NAME = your_database_name
DB_USER = your_db_user
DB_PASS = your_password
DB_PORT = your_port
```

## 📦 Docker Details
- 🗄️ **Local Database**: **PostgreSQL** running on port `5434` with persistent data storage.
- 🌐 **Web Application**: **Streamlit** app served at port `8501`.
- 📖 **Documentation**: **MkDocs** documentation served at port `8000`.
- 🐍 **Jupyter Notebook**: **Jupyter** server running on port `8888` for interactive development.
- 📂 **Volumes**: Data is persisted locally in the `./data` folder.

### 🐍 Jupyter Notebook Access
After starting the Jupyter Notebook service with `docker-compose up`, you will need to access it using a unique link generated each time the container is built. This link includes an authentication token for security.

To find the access link, check the terminal logs where Docker is running. You will see output similar to:

```bash
http://127.0.0.1:8888/?token=<your_token_here>
```

Copy and paste this link into your web browser to access the Jupyter Notebook.
