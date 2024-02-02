grill:
   poetry run pytest
   poetry run mypy lamr
   poetry run isort lamr --float-to-top
   poetry run black lamr
   poetry run ruff lamr --fix
  
md:
  npx prettier README.md --write
  npx prettier lamr/topics --write