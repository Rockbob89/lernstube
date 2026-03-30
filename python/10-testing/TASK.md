# Task 10: Testing

## Objective
Write proper tests with pytest.

## What to Learn
- `pytest` basics — test discovery, assertions, running tests
- `@pytest.fixture` — provides shared setup to tests that declare the fixture as a parameter; `scope` controls lifetime
  ```python
  @pytest.fixture(scope="module")   # created once per module, not per test
  def db():
      conn = create_connection()
      yield conn          # setup above yield, teardown below
      conn.close()

  def test_query(db):     # pytest injects `db` automatically
      assert db.query("SELECT 1") == [1]
  ```
- `@pytest.mark.parametrize` — runs the same test with multiple inputs
  ```python
  @pytest.mark.parametrize("a, b, expected", [(1, 2, 3), (0, 0, 0), (-1, 1, 0)])
  def test_add(a, b, expected):
      assert add(a, b) == expected
  ```
- `unittest.mock` — replace real objects with controlled fakes; `patch` is a decorator/context manager that substitutes a name temporarily
  ```python
  from unittest.mock import patch, MagicMock

  def test_calls_api():
      with patch("mymodule.requests.get") as mock_get:
          mock_get.return_value = MagicMock(status_code=200, json=lambda: {"ok": True})
          result = my_function()
      mock_get.assert_called_once()
  ```
- What to test vs what not to test

## Exercise

Write tests for your `configlib` package from task 9.

```
python/10-testing/
├── conftest.py          # shared fixtures
├── test_models.py       # test AppConfig
├── test_parser.py       # test load_config, parse_config
├── test_exceptions.py   # test exception messages and chaining
└── test_stack.py        # test Stack[T]
```

Requirements:
- Use `@pytest.fixture` for common test data (valid configs, invalid configs)
- Use `@pytest.mark.parametrize` for `parse_config` — test multiple invalid inputs in one test function
- Test that exceptions raise with correct messages using `pytest.raises`
- Test edge cases: empty config, missing keys, wrong types, empty stack pop
- All tests must pass with `pytest -v`
