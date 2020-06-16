# Attempt 1

index.html, index.js and package.json all in the root directory where `vercel` was run:

### Details

- `app.use(express.static('.'))` in index.js to serve html on route `/`

- No `vercel.json` config file.

### Result

- index.html loads correctly, but can't access the routes. Likely because the index.js file not being run at all, and vercel is just serving the html file in the root. Understandable mistake on my part

---

# Attempt 2

Read the Vercel documentation, they say to put the API backend in an API folder, and it will work without any configuration

### Details

- index.js now in `api/`, and index.html is in `static/`. package.json in root directory.

- `app.use(express.static('./static'))` in index.js to serve html on route `/`

- No `vercel.json` config file.


### Result

- Going to the deployed site just gives me a file-explorer like thing that shows me the uploaded source. 

---

# Attempt 3

Maybe I need to actually use the `vercel.json` config file to point the routes at the index.js file...? Running out of ideas.

### Details

- `vercel.json` now contains:
    ```
    {
        "routes": [
            {
            "src": "/.*",
            "dest": "api/index.js"
            }
        ]
    }
    ```


### Result

- SOME PROGRESS, now going to the deployed site actually goes to the express backend!

- However, can't figure out why the index.html page isn't being served... 

- Also, hitting any of the actual end-points just gives me a 502 BAD_GATEWAY error

---

# Attempt 4

OK, it works on Heroku with everything in the root directory, maybe if I go back to attempt 1 but set up the `vercel.json` to point to the correct file location it will all magically work

### Details

- Attempt 1, with `vercel.json` "dest" field changes to `./index.js`

### Results

- Same as attempt 1.

---

# Overall comments

- The express code only seems to work when the file is placed in the `api/` folder, regardless of configuration of the `vercel.json` file.

- Can't figure out how to get it to serve the index.html (in this case not important to have it be served, but I would like to learn how).

- Can't figure out why I get a 502 error when I get the express stuff to work in attemp #3. Works fine locally with `npm run` / `npm run dev`