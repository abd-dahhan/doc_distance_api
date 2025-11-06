# Document Distance (AI Engineering concepts)


In the interest of time, do not implement authentication. Focus on the algorithms + deployment.
You will find the API logic has been placed in the `api_views.py` module (no need to rewrite it)

## Tasks to be completed in `algo.py`

**Very important to do before 12**
- Deploy a `render` webservice
- No database is necessary for this service (skip that step)

**You can do after 12**
- Add a CI/CD through GH actions.

Make the API endpoints work by implementing some algorithms:

1) `Text to list` api endpoint.


`POST /api/text-to-list/`

When a payload of text that looks like this:

```json
{
    "text": "Hello world, you are awesome"
}
```


I would like to see a response like this:

```json
{
    "response": ["hello", "world", "," "you", "are", "awesome"]
}
```


2) given an array of letters sent as a JSON, return an object (dictionary) with their frequencies.


`POST /api/get-frequencies/`

```json
{"payload": ["h", "e", "l", "l", "o"]}
```

The response should be:

```json
{"response": {"h": 1, "e": 1, "l": 2, "o": 1}}
```


[Difficulty level: Hard]

No API view and No URL has been created for this. This has been left as an exercise to the student.

Topics to learn (or research):
statistics => frequencies (number of times something appears in a collection)


3) Get the similarity of two separate words (later expanded to separate documents).

Our function, will use the outputs of `get_frequencies` or `get_letter_frequencies`.


Consider two lists

$$
L_1 = ["a", "b"], L_2 = ["b", "c"]
$$ 
then let `U` be a list made up for all elements (non repetitive) in L<sub>1</sub> and L<sub>2</sub>

$$
U = ["a", "b", "c"]
$$


For an element _e_ in L<sub>1</sub> or L<sub>2</sub>, let

![Similarity formula](formula.png)

We can then define it as follows:

δ(e) = |count(e, L<sub>1</sub>) − count(e, L<sub>2</sub> )| and σ(e) = count(e, L<sub>1</sub>) + count(e, L<sub>2</sub>).

The || (vertical bars) denote absolute value, if a value is negative it is converted to positive.


`Similarity` is defined as:

![Similarity formularit](similar_formula.png)

Here sums are taken over all the elements of `U` and the results are rounded off to two decimal places. 

$$
u_1, u_2, u_3, ...
$$


Caveat:

The tasks are designed in such a way to encourage you to think hard and take it slow. 
While deploying to the cloud is usually "easier" these days, the task of crafting algorithms is mostly lost to AI.

The problem sets are designed to encourage that freedom of thought.