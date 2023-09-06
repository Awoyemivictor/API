python3 -m venv venv - to create a virtual environment
source venv/bin/activate - to activate the virtual environment on the terminal
uvicorn main:app --reload - to run the server


# CRUD API STANDARD CONVENTIONS
- Create      [POST]          /posts            @app.post("/posts")
- Read        [GET]           /posts/:id        @app.get("/posts/{id}")
            [GET]           /posts              @app.get("/posts")
- Update      [PUT/PATCH]     /posts/:id        @app.put("/posts/{id})
*** Put will change the entire thing
*** Patch will only change the specific thing
- Delete      [DELETE]        /posts/:id        @app.delete("/posts/{id}")



