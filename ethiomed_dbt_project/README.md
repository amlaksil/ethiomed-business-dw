# Ethiopian Medical Business Data Warehouse DBT Project

This DBT (Data Build Tool) project is designed to transform raw data from the `ethiomed_table` into structured and aggregated tables suitable for analysis. The primary goals are to clean, standardize, and aggregate the data to provide meaningful insights.

## Project Structure

- `dbt_project.yml`: The configuration file for the DBT project.
- `models/`: Directory containing the SQL models for the project.
- `models/stg_ethiomed_table.sql`: This model stages the raw data from the `ethiomed_table`.
- `models/transform_ethiomed_table.sql`: This model transforms and aggregates the staged data.
- `models/schema.yml`: This file defines tests and documentation for the models.

## Getting Started

### Prerequisites

- Python installed
- DBT installed (`pip install dbt`)
- PostgreSQL database with the `ethiomed_table`

### Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/amlaksil/ethiomed-business-dw
   cd ethiomed_dbt_project
   ```

2. **Install DBT:**

   ```bash
   pip install dbt
   ```

3. **Configure the database connection:**

   Edit the `profiles.yml` file (usually located in the `~/.dbt/` directory) to configure the connection to your Postgres database:

   ```yaml
   ethiomed_dbt_project:
     target: dev
     outputs:
       dev:
         type: postgres
         host: <host>
         user: <user>
         password: <password>
         port: <port>
         dbname: <dbname>
         schema: <schema>
   ```

4. **Run DBT models:**

   ```bash
   dbt run
   ```

5. **Test DBT models:**

   ```bash
   dbt test
   ```

6. **Generate documentation:**

   ```bash
   dbt docs generate
   dbt docs serve
	 ```

### Resources:
- Learn more about dbt [in the docs](https://docs.getdbt.com/docs/introduction)
- Check out [Discourse](https://discourse.getdbt.com/) for commonly asked questions and answers
- Join the [chat](https://community.getdbt.com/) on Slack for live discussions and support
- Find [dbt events](https://events.getdbt.com) near you
- Check out [the blog](https://blog.getdbt.com/) for the latest news on dbt's development and best practices
