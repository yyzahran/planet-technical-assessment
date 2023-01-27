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
    <li><a href="#notes">Notes</a></li>
    <li>
      <a href="#challenges">Challenges</a>
      <ul>
        <li><a href="#challenge-1">Challenge 1</a></li>
        <li><a href="#challenge-2">Challenge 2</a></li>
        <li><a href="#challenge-3">Challenge 3</a></li>
        <li><a href="#challenge-4">Challenge 4</a></li>
      </ul>
    </li>
    <li><a href="#to-the-reviewers">To the reviewers</a></li>
  </ol>
<br />

### Intuition
After reading the guide and the documentation provided. I did some manual testing using Postman to get a feel of the request and response bodies. As per the guide, I was to use Python and I decided to use Pytest as a test framework because I know that the QA folks at Planet use it, so it gave me a chance to show my knowledge.
<br />

### Project Structure
- `modules/APIHelper.py` hosts methods for creating, getting, updating, and deleting saved searches.

- `TestFiles/` includes the test files I created for testing.

- `tests/test_base.py` is the base class for the tests that includes the base url and the authorization.

- `tests/test_create_saved_search.py` includes tests for creating a new saved search, validating authorization and field entries.

- `tests/test_update_saved_search.py` includes tests for updating different fields of a saved search.

- `tests/test_delete_saved_search.py` includes tests for deleting a saved search.

- `tests/test_end_to_end.py` includes end-to-end tests for the flow of creating, updating, and deleting a saved search.

- `conftest.py` is the pytest configuration file. I added global fixtures there to prevent duplication in the test files and added a variables storage class so I can use the saved search id across multiple tests.

- `constants.py` has the API Key ONLY locally.
<br />

### Approach
I started by writing helper methods in `APIHelper` class to adhere to the DRY principle and not call the requests library api methods in multiple places and in the tests. This is to improve the maintainability and reliability of the code. I added a test base class as a parent to include the authorization for the requests and base url so as not to add it to every test file/class.

After doing some research and going through the documentation, I crafted a request body in `ExampleBody1.json` to use for testing, later I added `ExampleBody2.json` for the end-to-end tests.

I then started working on the `create` test cases and added as much as I saw fit. In most cases, I grouped several assertions in the same test and did not spread them out for the sake or readability and scalability of the project. After that I added the `delete` and `update` test cases. Later on when I felt comfortbale enough with the tests I had, I added an end-to-end flow.

For the `update` tests, I opted for editing/updating fields in the tests as needed as opposed to creating a different test file for each field entry to prevent clutter and to give more control to the tests for maintainability  and executability purposes.

Lastly, I added jsonschema validation methods and assertions to verify the reponse schema when creating a saved search.

<br />

### Notes

The API Key is not on the repository for security, so that only those who have the API key can use the tests and connect to the API endpoints.

I did not add tests to udpate `item_type` value as it the type was explicitly mentioned in the quide as PSSense.

<br />

## Challenges

In this section, I'll discuss breifly the major challneges that I faced while working on the assessment. I'd be willing to discuss this more in the next stage if I get the chance.

### Challenge 1
In the `response_schema` in `conftest.py`, I was having troubles with asserting the GET response schema as the `last_executed` field should be of type string, but it always returned `None`. That was because all the searches I create for testing are 'dummy' and not actually used so I added the type of that field in the schema to be `null`. I verified that other real-life saved searched has the proper `last_-_executed` field by calling the list searches endpoint (https://api.planet.com/data/v1/searches) and checking that that field in of type `string` when used.
### Challenge 2
I tried to utilize helper methods and fixtures as much as I could as well as adding global variables whenever I can. However, I didn't want to go overboard so as not to affect the readability of the project. For example, I thought about adding global parameters with the different status codes I expected, but I felt that that would be confusing and the user/reviewer will have to resort back to different files to check what each variable means. Sometimes leaving parameters compartmentalized within the test can be easier to maintain.
### Challenge 3
I opted for making the most out of every test by adding more than just one assertion instead of adding each assertion to a separate test for the sake of scalability and executability  of the project. For example, in a test case where I'd test creating a saved search, I create the search, then assert its GET response and validate its schema instead of adding the latter two in other separate tests.

### Challenge 4

<br />

## To the reviewers
Thanks a lot for reading this and for the opportunity. I hope you enjoy going through the project as much as I enjoyed working on it.