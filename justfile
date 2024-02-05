grill:
   poetry run pytest
   poetry run mypy lamr
   poetry run isort lamr --float-to-top
   poetry run black lamr
   poetry run ruff lamr --fix
  
md:
  npx prettier README.md --write
  npx prettier lamr/topics --write
  npx prettier docs/* --write

docs:
  npm run docs:dev  

docs-publish:
  npx vitepress build docs
  poetry run ghp-import -np docs/.vitepress/dist

publish:
  poetry publish --build
  
