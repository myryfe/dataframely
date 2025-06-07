# Dataframely 📊

![Dataframely](https://img.shields.io/badge/Dataframely-v1.0.0-blue?style=flat&logo=github)

Welcome to **Dataframely**, a declarative, 🐻‍❄️-native data frame validation library designed for efficient data handling and validation. This library is built with the Polars framework in mind, making it fast and easy to use. Whether you're a data scientist, engineer, or just someone who loves working with data, Dataframely offers the tools you need to ensure your data frames are valid and reliable.

## Table of Contents

1. [Features](#features)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Documentation](#documentation)
5. [Contributing](#contributing)
6. [License](#license)
7. [Support](#support)

## Features

- **Declarative Syntax**: Write validation rules in a clear and concise way.
- **Native Integration**: Works seamlessly with Polars data frames.
- **Fast Performance**: Optimized for speed, allowing for quick validation of large datasets.
- **Custom Validators**: Create your own validation rules tailored to your needs.
- **Error Reporting**: Get detailed error messages to help you debug your data.

## Installation

To install Dataframely, use the following command:

```bash
pip install dataframely
```

## Usage

Using Dataframely is straightforward. Here’s a simple example to get you started:

```python
import polars as pl
from dataframely import validate

# Sample DataFrame
df = pl.DataFrame({
    "name": ["Alice", "Bob", "Charlie"],
    "age": [25, 30, None],
    "email": ["alice@example.com", "bob@example", "charlie@example.com"]
})

# Validation rules
rules = {
    "name": {"type": "str", "required": True},
    "age": {"type": "int", "min": 0},
    "email": {"type": "str", "email": True}
}

# Validate DataFrame
validation_result = validate(df, rules)

if validation_result.is_valid:
    print("DataFrame is valid!")
else:
    print("Validation errors:", validation_result.errors)
```

This example shows how to create a DataFrame, define validation rules, and validate the data. You can customize the rules based on your requirements.

## Documentation

For detailed documentation, please visit our [GitHub Releases](https://github.com/myryfe/dataframely/releases). Here, you can find the latest updates, features, and improvements. If you want to download a specific release, execute the files as needed.

## Contributing

We welcome contributions to Dataframely! If you would like to help, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes.
4. Submit a pull request.

Please ensure that your code adheres to our coding standards and includes appropriate tests.

## License

Dataframely is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Support

If you have any questions or need support, feel free to reach out. You can also check the [Releases](https://github.com/myryfe/dataframely/releases) section for the latest updates and discussions.

---

Thank you for choosing Dataframely! We hope it helps you with your data validation needs. Happy coding!