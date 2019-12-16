## Phase 2 Assessment

#### Take-Home portion: (4 points out of 10 total)

* Submit your code for the take-home portion of the exam. Give the grader
your flask code and the src folder of your react frontend.

#### Problem 1 (1 point)

* Write an API server in Flask that serves the following two endpoints:

```
curl 127.0.0.1:5000/  (GET request)

responds with '{"message": "hello"}'

a POST request to 127.0.0.1:5000/evens with json data like
'{"values": [1,2,3,4,5]}'

should respond with '{"evens": 2}'

a POST request to 127.0.0.1:5000/odds with json data like
'{"values": [1,2,3,4,5]}'

should respond with '{"odds": 3}'

(the api returns either the number of even or the number of odd numbers in the input)
```

For testing, you can use:

```bash curl -d '{"values":[1,2,3,4,5]}' -H "Content-Type: application/json" -X POST http://localhost:5000/<route to test>```

#### Problem 2 (2 points)

* in plain javascript & html, create a page with a button labeled 'triangle' and a text entry field where the user can input a number.

When clicked it should create text output to an html element like the following:

```
*
**
***
****
*****
******
*******
```

with a number of rows equal to the value in the input field (the nth row should
have n * symbols in a row.

Note: `<br/>` is the html element for a newline

* If you need to, used a fixed number or console.log for partial credit

#### Problem 3 (3 points)

Create a React app with two routes, the root path and a route '/people'

There should be a nav bar that is displayed on both pages with a link to home and a link
to people

The home route should have a title that says 'Welcome' and have some multi-paragraph text (use
lorem ipsum or copy and paste anything you want, it just needs multiple paragraph elements)

The /people route should have a form with a firstname field, a lastname field, and a
button that says 'add' and a button that says 'reset'

Create a Person component that displays a firstname and a lastname as received in its props.

/people should show a list of all people added to the list so far (filling in a
first name and a last name and clicking add will cause there to be a new Person element
displayed below the existing ones.

Clicking reset empties the list of people.

#### Bonus (up to 1 point)

You can gain bonus credit for doing the following:

* Use css to style your answer to problem 3. The paragraphs at the home route should have a maximum width and space between each other. The nav should have a different color than the rest of the page. The Person elements should have a border. Any extra flourishes are nice.

