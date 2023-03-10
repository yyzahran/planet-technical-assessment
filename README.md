<a name="readme-top"></a>
<h1 align="center">Planet's Technical Assessment</h1>

  <p align="center">
    A Python-based test framework that automates the objectives outlined by Planet in the guide.
    <br />
    <br />
  </p>
</div>

  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>

## About The Project

This is Python/Pytest-based project that automates testing creating, updating, and deleting saved searches as outlined by Planet.

For more about the through process of going through the project, please check <a href="https://github.com/yyzahran/planet-technical-assessment/blob/master/ThoughtProcess.md">ThoughtProcess.md</a>.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Getting Started

This section is to walk you through the setup for running the tests.

### Prerequisites

You'll need Python 3+ to run the project.

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/yyzahran/planet-technical-assessment.git
   ```
2. Install requirements
   ```sh
   pip3 install -r requirements.txt
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Usage

In `constants.py`, update the value of `PL_API_KEY` with the proper API key. It isn't included in the repository for security reasons.

Use any of the following commands to run tests as needed:
- Run tests using pytest with verbose
   ```sh
   python3 -m pytest -v
   ```
- Run tests with the `print` statements output
   ```sh
   python3 -m pytest -v -s
   ```
- Run tests of a specific file
   ```sh
   python3 -m pytest /path/to/test/file -v
   ```
- Run tests and output results to a file
   ```sh
   python3 -m pytest -v -s > test_log.log
   ```

For more info about pytest's usage, check the [documentation](https://docs.pytest.org/en/6.2.x/usage.html).

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Contact

Youssef Zahran - youssefyzahran@gmail.com - [LinkedIn](https://www.linkedin.com/in/youssef-zahran-15894772/)

Project link: [https://github.com/yyzahran/planet-technical-assessment](https://github.com/yyzahran/planet-technical-assessment)

<p align="right">(<a href="#readme-top">back to top</a>)</p>
