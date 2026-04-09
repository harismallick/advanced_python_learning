# Video source: https://youtu.be/Qu3dThVy6KQ?si=RQYSrDhGhPXVENkm
import itertools
from operator import mul

def count_example() -> None:
    """ 
    The count method returns an iterable that provides an auto incrementing 
    integer value.
    """

    counter = itertools.count() # By default starts at 0

    # It is a generator so can be used with next()
    # print(next(counter))
    # print(next(counter))
    # print(next(counter))
    # print(next(counter))

    data = [100, 200, 300, 400]
    zip_example1 = list(zip(itertools.count(), data))
    print(zip_example1)

    zip_example2 = list(zip(itertools.count(start=10, step=10), data))
    print(zip_example2)
    # zip's behaviour is to stop iterating when the shortest iterator has been exhausted.
    # To keep iterating until the longest iterator is exhausted, use itertool's zip_longest
    return

def zip_longest_example() -> None:
    """
    Combine two iterables into one until the longest iterable is exhausted.
    """
    data = [100, 200, 300, 400]
    zip_example = list(itertools.zip_longest(range(10), data))

    print(zip_example)
    # zip_longest adds None values once the shortest iterator has been exhausted.
    return

def cycle_example() -> None:
    """
    Cycles through set values in an iterable.
    Once the last value is used, it cycles back to the first value in the iterable.
    This iterator never becomes exhausted.
    Useful for toggling between set states, in a finite state machine, for example.
    """
    counter = itertools.cycle(('ON', 'OFF'))
    switch_events = 6
    while switch_events > 0:
        print(f"The current state is {next(counter)}")
        switch_events -= 1
    return

def repeat_example() -> None:
    """
    Repeat the same value indefinitely or a finite number of times.
    """
    counter = itertools.repeat(2, times=3)

    for count in counter:
        print(f"Times iterated through: {count}")

    # Once the times=3 limit is reached, StopIteration error will occur    
    return

def starmap_example() -> None:
    """
    Variation of the map method where the arguments for a callable function are 
    packed into a tuple, rather than being passed individually to the map function
    """
    squares = itertools.starmap(pow, [(1, 2), (2, 2), (3, 2), (4, 2)])
    print(list(squares))
    # the pow function takes in two values, the exponent and the base
    # These two values were packed into a tuple
    return

def combinations_example() -> None:
    """
    Return all possible unique combinations from a list of values.
    The order of the items in the combination is NOT considered.
    A,B and B,A are considered the same.
    """
    letters: list[str] = ['a', 'b', 'c', 'd']
    results = itertools.combinations(letters, 2) # return all unique 2-letter combinations
    print(f"All combinations of {letters}")
    for result in results:
        print(result)
    return

def permutations_example() -> None:
    """
    If the order of elements in the grouping is important, then use permutations 
    rather than combinations. Here, A,B is a different permutation than B,A
    """
    letters: list[str] = ['a', 'b', 'c', 'd']
    results = itertools.permutations(letters, 2) # return all unique 2-letter combinations
    print(f"All permutations of {letters}")
    for result in results:
        print(result)
    return

def product_example() -> None:
    """
    Both combinations and permutations ONLY use each element in the iterable once.
    If you need to compute all possible permutations including repeating an element
    multiple times, then product is the itertools method of choice.

    Gives the cartesian product of given iterables. Equivalent to running nested
    for loops. Creating multiple nested for loops with the same iterable requires
    using the 'repeat' parameter.
    """

    numbers: list[int] = [0,1,2,3]
    results = itertools.product(numbers, repeat=3)
    print(f"All possible 3-digit permutations of {numbers}")
    for result in results:
        print(result)
    
    return

def combinations_w_replacement_example() -> None:
    """
    Compute all possible combinations of elements in an iterable with the same
    element allowed to be used more than once.
    """

    numbers: list[int] = [0,1,2,3]
    results = itertools.combinations_with_replacement(numbers, 3)
    print(f"All possible 3-digit combinations of {numbers} with replacement allowed")
    for result in results:
        print(result)
    
    return

def chain_example() -> None:
    """
    Chain multiple iterables together into a single iterable.
    """
    list1: list[str] = ['a','b','c','d']
    list2: list[str] = ['e','f','g','h']
    list3: list[str] = ['i','j','k','l']

    chained = itertools.chain(list1, list2, list3)
    for element in chained:
        print(element)
    return

def islice_example() -> None:
    """
    Only iterate through a slice of the complete iterable.
    This might be useful when you only want to iterate through particular lines
    in a list of files and any situation where iterating through the complete iterable
    would waste compute.
    """
    example_list = [x for x in range(50)]
    slice1 = itertools.islice(example_list, 0, 25, 2)
    # The parameter ints are start index, stop index and step for the slice.
    # If no slice indices are given, will iterate through the whole parent iterable
    
    print([num for num in slice1])
    return

def compress_example() -> None:
    """
    Filters elements from a parent iterable based on a supplementing selector
    iterable containing boolean values for each element in the parent iterable.

    Compress requires two iterables.
    """
    list1: list[str] = ['a','b','c','d']
    selector: list[bool] = [True, False, False, True]

    compressed_list = itertools.compress(list1, selector)
    print(f"The compressed list of elements is {[x for x in compressed_list]}")

    return

def is_even(num: int) -> bool:
    return num % 2 == 0

def filter_false_example() -> None:
    """
    The regular filter method in Python filters for truthy condition.
    If you want to filter for falsy condition, then use this method.
    Both methods require a helper function containing the filter logic.
    """
    numbers_list = [1,2,3,4,5]
    even_nums = filter(is_even, numbers_list)
    print(f"Even numbers: {[x for x in even_nums]}")

    odd_nums = itertools.filterfalse(is_even, numbers_list)
    print(f"Odd numbers: {[x for x in odd_nums]}")
    return

def is_less_than_three(num: int) -> bool:
    return num < 3

def dropwhile_takewhile_example() -> None:
    """
    These methods keep iterating through an iterable until a certain conditions
    is TRUE. Once a conditional fails, these two methods behave slightly differently:

    dropwhile ONLY returns elements AFTER the first instance of false conditional.

    takewhile returns elements from the iterable UNTIL the first false conditional.
    """
    numbers_list = [1,2,3,4,5]
    dropwhile = itertools.dropwhile(is_less_than_three, numbers_list)
    print(f"{numbers_list} after dropwhile: {[x for x in dropwhile]}")

    takewhile = itertools.takewhile(is_less_than_three, numbers_list)
    print(f"{numbers_list} after takewhile: {[x for x in takewhile]}")
    return

def accumulate_example() -> None:
    """
    Maintains a running tally of a select mathematical operation performed on all
    elements in the iterable.
    By default, addition is the operation.
    Import the operator module with the operation of choice and pass as a parameter
    to the accumulate itertool.
    """
    numbers_list = [1,2,3,4,5]
    running_sum = itertools.accumulate(numbers_list)
    print(f"Sum after each element in the iterable: {[x for x in running_sum]}")

    running_mul = itertools.accumulate(numbers_list, mul)
    print(f"Sum after each element in the iterable: {[x for x in running_mul]}")
    return

def pairwise_example() -> None:
    """
    This itertool computes the difference between neighbouring elements in the 
    parent iterable.
    """
    # Temperatures in degrees Celsius for a week
    temps = [18, 20, 23, 21, 19, 24, 25]

    print(f"{'Day Change':<15} | {'Difference'}")
    print("-" * 30)

    # pairwise(temps) yields: (18, 20), (20, 23), (23, 21)...
    for current_day, next_day in itertools.pairwise(temps):
        diff = next_day - current_day
        direction = "Rise" if diff > 0 else "Drop"
        print(f"{current_day}°C to {next_day}°C | {direction} of {abs(diff)}°C")
    return

def tee_example() -> None:
    """
    Creates copies of the parent iterable. Once tee is used to create copies, ONLY
    the copies should be iterated. The parent iterable should NOT be iterated through.
    Why?
    The Rule: If you advance the parent, the children lose those items. 
    If you use the children, they maintain their own separate buffers to ensure they each see every item.
    """
    parent = ["apple", "banana", "grape"]

    l1, l2 = itertools.tee(parent, 2)
    for fruit in l1:
        print(fruit)

    for fruit in l2:
        print(fruit[::-1])
    return

def get_state[T](person: dict[str, T]) -> T:
    return person['state']

def groupby_example() -> None:
    """
    Groups CONSECUTIVE elements in an iterable that share the same key.
    As a result, groupby only works with a sorted list of elements.
    """

    people = [
        {
            'name': 'John Doe',
            'city': 'Gotham',
            'state': 'NY'
        },
        {
            'name': 'Jane Doe',
            'city': 'Kings Landing',
            'state': 'NY'
        },
        {
            'name': 'Corey Schafer',
            'city': 'Boulder',
            'state': 'CO'
        },
        {
            'name': 'Al Einstein',
            'city': 'Denver',
            'state': 'CO'
        },
        {
            'name': 'John Henry',
            'city': 'Hinton',
            'state': 'WV'
        },
        {
            'name': 'Randy Moss',
            'city': 'Rand',
            'state': 'WV'
        },
        {
            'name': 'Nicole K',
            'city': 'Asheville',
            'state': 'NC'
        },
        {
            'name': 'Jim Doe',
            'city': 'Charlotte',
            'state': 'NC'
        },
        {
            'name': 'Jane Taylor',
            'city': 'Faketown',
            'state': 'NC'
        }
    ]

    person_group = itertools.groupby(people, get_state)

    for key, group in person_group:
        print(key, len(list(group)))
    return

def main() -> None:
    # count_example()
    # zip_longest_example()
    # cycle_example()
    # repeat_example()
    # starmap_example()
    # combinations_example()
    # permutations_example()
    # product_example()
    # combinations_w_replacement_example()
    # chain_example()
    islice_example()
    compress_example()
    filter_false_example()
    dropwhile_takewhile_example()
    accumulate_example()
    pairwise_example()
    tee_example()
    groupby_example()
    return

if __name__ == "__main__":
    main()