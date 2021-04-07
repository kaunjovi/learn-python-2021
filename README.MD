
# Say Hello world with Python :) 

```python
def main():
    print("Hello World!")

if __name__ == "__main__":
    main()
```

# Is there a recommended folder structure with Python3 ? 

Python doesn't have a distinction between /src , /lib , and /bin like Java or C has. 
Since a top-level /src directory is seen by some as meaningless, your top-level directory can be the top-level architecture of your application. 
I recommend putting all of this under the "name-of-my-product" directory.

Doesn't too much matter. Whatever makes you happy will work. There aren't a lot of silly rules because Python projects can be simple.

/scripts or /bin for that kind of command-line interface stuff
/tests for your tests
/lib for your C-language libraries
/doc for most documentation
/apidoc for the Epydoc-generated API docs.
And the top-level directory can contain README's, Config's and whatnot.

The hard choice is whether or not to use a /src tree. Python doesn't have a distinction between /src, /lib, and /bin like Java or C has.

Since a top-level /src directory is seen by some as meaningless, your top-level directory can be the top-level architecture of your application.

/foo
/bar
/baz
I recommend putting all of this under the "name-of-my-product" directory. So, if you're writing an application named quux, the directory that contains all this stuff is named  /quux.

- https://stackoverflow.com/questions/193161/what-is-the-best-project-structure-for-a-python-application

# Is there something like maven or grade that will do the project folder set up for me in Python3 

- https://stackoverflow.com/questions/3324108/maven-equivalent-for-python
- There does not seem to be a yes. At least not a clear and straightforward one. 


# Variable declaration in Python 

- [How to Use Static Type Checking in Python 3.6](https://medium.com/@ageitgey/learn-how-to-use-static-type-checking-in-python-3-6-in-10-minutes-12c86d72677b)
- 




# Learning Python in 2021 

- [self](https://github.com/kaunjovi/learn-python-2021)

- Install the latest. With Homebrew. 
- Use one of the virtual env managers. pipenv
- Is there a standard folder structure for python projects ? 
    - if not, there should be 
    
# Kuber 

- MTO data 
    - Download raw data 
    - Filter only EQ data. Stamp date column. 
    - Reports 
        - 
- Filter only watchlist
    - 



# Rough notes 

- Installing 3 on macOS
- Installing Python 3 on macOS
- https://flaviocopes.com/python-installation-macos/
- 
- macOS installs Python 2 (outdated) by default, 
- for compatibility reasons, 
- making it available as /usr/bin/python.
- 
- If you install Xcode, the Apple Development IDE, it installs Python 3 in /usr/bin/python3. 
- In this case you can run python3 on your terminal to check the exact version installed, and if it’s recent - enough you might be already set up.
- 
- Python 3 is the one we’re going to use for modern Python development.
- One option is to use Homebrew to install the latest Python release.
- When it’s finally installed, Python is installed as /usr/bin/python3
- 
- However you have little control over the version number you run, as Apple updates it only with new Xcode - releases.


