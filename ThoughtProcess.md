Here I'll walk you through the approach I took while working on the assessment.
<br />
<!-- TABLE OF CONTENTS -->
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#intuition">Intuition</a>
    </li>
    <li><a href="#project-structure">Project Structure</a></li>
    <li><a href="#approach">Approach</a></li>
    <li>
      <a href="#test-cases">Challenges</a>
      <ul>
        <li><a href="#test-case-1">Challenge 1</a></li>
        <li><a href="#test-case-1">Challenge 2</a></li>
        <li><a href="#test-case-1">Challenge 3</a></li>
        <li><a href="#test-case-1">Challenge 4</a></li>
        <li><a href="#test-case-1">Challenge 5</a></li>
        <li><a href="#test-case-1">Challenge 6</a></li>
      </ul>
    </li>
    <li><a href="#to-the-reviewers">To the reviewers</a></li>
  </ol>
<br />

### Intuition
After reading the guide and reading the documentation provided. I did some manual testing using postman to get a feel of the request and response bodies. As per the guide, I was to use Python and I decided to use Pytest as a test framework because I know that the QA folks at Planet use it, so it have me a chance to show my knowledge.
<br />

### Project Structure
- `modules/APIHelper.py` hosts methods for creating, getting, updating, and deleting saved searches by utilizing the `requests` library to prevent code duplication and calling the requests multiple times in different places.

- `TestFiles/` includes the test files I needed for testing. I opted for editing/updating fields in the tests as needed as opposed to creating a different test file for each field entry to prevent clutter and to give more control to the tests for maintainability  and executability purposes.

- `tests/test_base.py` is the base class for the tests that includes the base url and the authorization.

- `tests/test_create_saved_search.py` includes tests for creating a new saved search, validating authorization and field entries.

- `tests/test_update_saved_search.py` includes tests for updating different fields of a saved search.

- `tests/test_delete_saved_search.py` includes tests for deleting a saved search.

- `tests/test_end_to_end.py` includes end-to-end tests for the flow of creating, updating, and deleting a saved search.

- `conftest.py` is the pytest configuration file. I added a global fixture there to prevent duplication in the test files and added a variables storage so I can use the saved search id across multiple tests.

- `constants.py` has the API Key ONLY locally for security.
<br />

### Approach
I started by writing helper methods in `APIHelper` class to adhere to the DRY principle and not call the requests library api methods in multiple places and in the tests. This is to improve the maintainability and reliability of the code.

After doing some research and going through the documentation, I crafted a request body in `ExampleBody1.json` to use for testing, later I added `ExampleBody2.json` for testing purposes.

When starting the tests, I added a test base class as a parent to include the authorization for the requests and base url so as not to add it to every test file/class. From there, I was able to start writing test cases for creating, updating, and deleting saved searches. I usually write the happy scenarios first and then add the negative test cases to increase the coverage.

Lastly, I added jsonschema validation to verify the reponse schema when creating a saved search.

The API Key is not on the repository for security, so that only those who have the API key can use the tests and connect to the API endpoints.
<br />

## Challenges

In this section, I'll mention breifly the challneges that I faced while working on the assessment.

### Challenge 1
In the `response_schema` in `conftest.py`, I was having troubles with asserting the GET response schema as the `last_executed` field should be of type string, but it always returned `None`. That was because all the searches I create for testing are 'dummy' and not actually used so I added the type of that field in the schema to be `null`. I verified that other real-life saved searched has the proper `last_-_executed` field by calling the list searches endpoint (https://api.planet.com/data/v1/searches) and checking that that field in of type `string` when used.
### Challenge 2
I tried to utilize helper methods and fixtures as much as I could as well as adding global variables whenever I can. However, I didn't want to go overboard so as not to affect the readability of the project. For example, I thought about adding global parameters with the different status codes I expected, but I felt that that would be confusing and the user/reviewer will have to resort back to different files to check what each variable means. Sometimes leaving parameters compartmentalized within the test can be easier to maintain.
### Challenge 3
I opted for making the most out of every test by

### Challenge 4

<br />

## To the reviewers
Thanks a lot for reading this and for the opportunity. I hope you enjoy going through the project as much as I enjoyed working on it.