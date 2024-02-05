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
  poetry run lamr-publish code docs/code
  poetry run lamr-publish manual docs/manual
  npm run docs:dev  

ghp:
  npx vitepress build docs
  poetry run ghp-import -np docs/.vitepress/dist

publish:
  poetry publish --build
  
