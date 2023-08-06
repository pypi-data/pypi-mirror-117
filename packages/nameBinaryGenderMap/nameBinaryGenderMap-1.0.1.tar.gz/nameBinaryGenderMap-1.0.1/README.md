# nameBinaryGenderMap Package

The `nameBinaryGenderMap` package provides a module that can easily be used to find the corresponding binary gender class (i.e., male or female) for an input name. This package uses around ~100k entries of four gender name datasets provided by [catalog.data.gov](https://catalog.data.gov/).

---

### How to use the `nameBinaryGenderMap` module in python?


1) first import the `nameBinaryGenderMap` module as:
```
>>> import nameBinaryGenderMap as nbgm
```

2) then use the imported `nameBinaryGenderMap` module to check the binary gender assignment for your desired names using the `whats_the_gender()` function as:
```
>>> nbgm.whats_the_gender(name = "sara")
the binary gender assigned to 'sara' is 'female'

>>> nbgm.whats_the_gender(name = "john")
the binary gender assigned to 'john' is 'male'
```

---

### Notes:

- i) The `whats_the_gender()` is not sensitive to character capitalization, e.g., 
    ```
    >>> nbgm.whats_the_gender(name = "jOhN")
    the binary gender assigned to 'jOhN' is 'male'
    ```

- ii) The `whats_the_gender()` function can work for many non-English names too:
  - for instance let's check for two famous boy and girl names in __Chinese__ -> Boy: `Yichen` and Girl: `Yinuo`:
    ```
    >>> nbgm.whats_the_gender(name = "Yichen")
    the binary gender assigned to 'Yichen' is 'male'

    >>> nbgm.whats_the_gender(name = "Yinuo")
    the binary gender assigned to 'Yinuo' is 'female'
    ```

  - let's also check for two famous boy and girl names in __Middle East__ -> Boy: `Abbas` and Girl: `Aaminah`:
    ```
    >>> nbgm.whats_the_gender(name = "Abbas")
    the binary gender assigned to 'Abbas' is 'male'

    >>> nbgm.whats_the_gender(name = "Aaminah")
    the binary gender assigned to 'Aaminah' is 'female'
    ```