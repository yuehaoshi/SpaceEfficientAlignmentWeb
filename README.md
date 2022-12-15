# Space-efficient global/fitting/local alignment visualization
## Intro:
The website allows users to input two DNA sequences and select one alignment type (glocal, fitting, or local). The given two sequences will be aligned using space-efficient alignment algorithm in backend. The alignment result is then displayed on the web page with a (m+1)*(n+1) table where alignment path is highlighted. The display of input and result page can be found in figures below:
## Usage:
Clone the whole repository in your local, direct to the repository, run `flask run`. (You can also run `flask --debug run` for automatically update while running if you want to play with this web). Go to this address `http://127.0.0.1:5000` using your browser, and you should see the website deployed here.
The website should look like: 

![Screenshot 2022-12-14 at 23 34 14](https://user-images.githubusercontent.com/70357591/207780695-f3bfe9dd-f2fb-44de-aaae-339f5dd09e17.png) 

If you give two DNA sequences as input (note that you must only contain capitalized "A", "G", "C" and "T" in your sequence input) and select an alignment type (Global, Fitting or local). For example: 

![Screenshot 2022-12-14 at 23 36 38](https://user-images.githubusercontent.com/70357591/207781040-5a7a14b9-e749-470d-9da6-04820e64423d.png) 

After click `Show Table` button, you should get your alignment result as follows: 

![Screenshot 2022-12-14 at 23 37 25](https://user-images.githubusercontent.com/70357591/207781137-73b41e48-de8b-47a0-9b00-09c320ce9bd8.png) 

## Note:
This alignment is using:
- score function:  
  - 1 for matching
  - -1 for substitution 
  - -1 for indel penalty  

- Alphabet:
  - A, G, C, T
You can customize scoring functino and alphabet in `main.py` by modifying this part:
```python
# Change this line to customize your Alphabet:
keys = ['A', 'C', 'T', 'G', '-']
# Change following lines to customize your scoring function
delta = {}
for i in range(len(keys)):
    delta[keys[i]] = {k : v for (k,v) in zip(keys, [1 if keys[i] == keys[j]  else -1 for j in range(len(keys))])}

```

Have fun! ^_^
