# definitely
Typing tricks that make your type checker *a little* more quiet.

**Key features**:
- `definitely` – Type everything as you wish.
- `asyncily` – Run a function asynchronously.
- `asyncily_iterate` – Iterate through an iterator asynchronously.
- `reversely` – Reverse a dictionary.

```haskell
pip install definitely-typed
```

I should all be responsible about this, admittedly. Sorry guys.

## Methods
They just exist!

### <kbd>def</kbd> definitely
Definitely typed.

```python
person = "Charles"

# Transforms `person` into any type you desire
assert definitely(person, int)

reveal_type(person)
#           ^^^^^^
# runtime:     str
# typecheck:   int
```

The runtime type **WILL NOT** change, yet when `TYPE_CHECKING`, the variable acts just like the desired type (in this case, `int`).

### <kbd>def</kbd> asyncily
Asynchronously run a function.

```python
# You can use this as a decorator like so:
@asyncily
def buy_stuff(item: str):
    print("dad is going out!")
    time.sleep(2 << 40)
    print("came back with the %s!" % item)

await buy_stuff("milk")

# Or, you can use this as a "async function factory" like so:
def make(name: str):
    return f"Made product: {name!r}"

amake = asyncily(make)
await amake("milk")
```

### <kbd>def</kbd> asyncily_iterate
Asynchronously iterate through an iterator.

```python
def get_resources():
    yield from ["banana", "guava", "apple"]

async for resource in asyncily_iterate(get_resources()):
    print("-", resource)

# Output:
# - banana
# - guava
# - apple
```

### <kbd>def</kbd> reversely
Reverse a dictionary.

```python
metadata = {"password": 1234, "total_users": 100_000}
reversed_metadata = reversely(metadata)

assert reversed_metadata == {1234: "password", 100_000: "users"}

reveal_type(reversed_metadata)
#           ^^^^^^^^^^^^^^^^^
# runtime:     dict[int, str]
# typecheck:   dict[str, int]
```

***

(c) 2024 AWeirdDev, and other silly people
