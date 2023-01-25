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
      <a href="#test-cases">Test Cases</a>
      <ul>
        <li><a href="#test-case-1">Test Case 1</a></li>
        <li><a href="#test-case-2">Test Case 2</a></li>
        <li><a href="#test-case-3">Test Case 3</a></li>
        <li><a href="#test-case-4">Test Case 4</a></li>
        <li><a href="#test-case-5">Test Case 5</a></li>
        <li><a href="#test-case-6">Test Case 6</a></li>
      </ul>
    </li>
    <li><a href="#to-the-reviewers">To the reviewers</a></li>
  </ol>
<br />

### Intuition
After reading the guide provided and going through the tests manually to get an idea about what I will be looking for. I decided to work on the Selenium framework using Java; I chose also to use TestNG as a testing framework and added a behaviour-driven development component using Cucumber to make the project suitable to tech and non-tech reviewers as I was instructed.

<br />

### Project Structure
- `src/CucumberRunner/` hosts the cucumber test runner for testing the features

- `src/feature/` includes six features corresponding to the six test cases

- `src/pages/` hosts `HomePage` and `PageBase` files for the Page Object Model (POM) design pattern

- `src/stepdefinition/` includes the methods for each step of the features

- `src/tests/` includes `TestBase` and the test classes for each test case

- `test-output/` (not in repo - appears locally after running tests) includes TestNG reports after running tests: `index.html` and `emailable-report.html`

- `target/`  (not in repo - appears locally after running tests) includes TestNG reports after running cucumber tests: `cucumber.html` and `cucumber.json`

- `pom.xml` contains all the dependencies needed for the Maven project
<br />

### Approach
I went with a POM design pattern to make the project concise. I housed all web elements and interacting methods I needed in `src/pages/HomePage` which extends `src/pages/PageBase` that includes a PageFactory class to support the POM design. It gave me access to the `initElements` method to initialize web elements and the annotation `@FindBy` to locate and declare web elements using the proper locators.

As for the tests in `src/tests`, each one includes the test steps outlined by the guide and extends `TestBase` that has the `setUp()` and `tearDown()` methods. In `setUp`, I handled getting `QE-index.html`'s relative path to make it cross-platform compatible. I worked on cross-browser testing by adding more than one browser option to increase the coverage which came in handy actually in test case 5 as will be mentioned. The browsers are Chrome, Safari, Firefox and Selenium's HtmlUnit headless browser. The `teardown` method closes the browser.

After I was done with the tests using the POM framework. I started converting my work into a more friendly format to be easy to read by non-developers. In other words, I started working on Cucumber features. It wasn't that hard converting the tests although I had to break them down more to fit the features' statements. Same as the tests, all the features are run on four browsers. The Cucumber test runner `TestRunner` functions same as `TestBase`.

I developed and tested the project on macOS and tested it on Linux Ubuntu.

<br />

## Test cases

In this section, you'll see how I tackled each of the test cases/objectives provided.

### Test Case 1
Asserted the email input, password input, and sign in button elements are displayed by using their selectors and utilizing the `isDisplayed()` method of web elements. Then sent strings to both inputs using the `sendKeys()` Selenium method.

### Test Case 2
Used a CSS selector to get the web elements of the list and defined them in a `List`. From there I got its size and asserted it to be 3.

The next part was tricky because using the method `getText()` would return both the value and the badge of the list element. I was able to solve this using `JavascriptExecutor` to get the text of each child node of the two, then assert them against pre-defined strings.

### Test Case 3
On first glance, the dropdown menu would appear to be of type `select`. However, it is a `button`. Once this is out of the way, the rest of the objective was straight forward, I got the text of the button and asserted it. Then I clicked the button to display the other `a` elements and clicked the third one - "Option 3".

### Test Case 4
Pretty straight-forward objective. Asserted that the first button's `isEnabled()` method to be `true`, while that of the second button to be `false`.

### Test Case 5
Since the guide mentioned that the delay was 'random'. I decided to handle this wait for the button appearance using a Java-oriented solution instead of using a Selenium implicit or explicit wait. If I try to click the button when it was not displayed, it'd give back an `ElementNotInteractableException` exception. From there, I handled that exception using a while loop that tries to click the button and breaks out of the loop when it's actually clicked.

After that, I would assert that the message `isDisplayed()` and the button is no longer enabled. This was working seamlessly on Chrome and Firefox browsers. However, when I started testing on Safari, it was failing because Safari is so fast it doesn't detect that the message was there. I was thinking about adding a sleep of a second or so as this would be enough, but then I implemented an explicit wait till the success message is visible before asserting that it's displayed and asserting that the button is not enabled.

### Test Case 6
I wrote the function `cellValue(int rowNum, int columnNum)` that takes row and column numbers and returns the value of the cell at that number from the table in the sixth div using `getText()`.
<br />

## To the reviewers
Thanks a lot for reading this and for the opportunity. I hope you enjoy going through the project as much as I enjoyed working on it.