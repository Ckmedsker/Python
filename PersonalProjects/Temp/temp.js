server.post("/create", checkUser, (req, res) => {
  Recipes.find()
    .sort({ createdAt: -1 })
    .then((result) => {
      const uniqueIngredients = [];
      result.forEach((recipe) => {
        recipe.ingredients.forEach((ingredient) => {
          if (!uniqueIngredients.includes(ingredient)) {
            uniqueIngredients.push(ingredient);
          }
        });
      });
      uniqueIngredients.sort();
      
      let ingredientsList = [];
      if (req.body.ingredients.length !== 0) {
        req.body.ingredients.forEach((ingredient) => {
          ingredientsList.push(ingredient);
        });
      }
      
      if (req.body.newIngredients.length !== 0) {
        const rawNewIngredients = req.body.newIngredients.split(",");
        rawNewIngredients.forEach((newIngredient) => {
          const trimmedIngredient = newIngredient.trim();
          if (!uniqueIngredients.includes(trimmedIngredient)) {
            ingredientsList.push(trimmedIngredient);
          }
        });
      }
      
      if (req.body.description === "") {
        req.body.description = "No description available.";
      }
      
      const userId = res.locals.user ? res.locals.user._id : null;
      User.findById(userId)
        .sort({ createdAt: -1 })
        .then((result) => {
          const username = result.email;
          
          const newRecipeInfo = {
            name: req.body.name,
            author: username,
            description: req.body.description,
            dishType: req.body.dishType,
            difficulty: req.body.difficulty,
            instructions: req.body.instructions,
            ingredients: ingredientsList,
          };
          
          const newRecipe = new Recipes(newRecipeInfo);
          newRecipe
            .save()
            .then((result) => {
              res.redirect("/");
            })
            .catch((err) => {
              console.log(err);
              res.status(500).json({
                error: "An error occurred while creating the recipe.",
              });
            });
        });
    })
    .catch((err) => {
      console.log(err);
      res.status(500).json({
        error: "An error occurred while fetching existing recipes.",
      });
    });
});