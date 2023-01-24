list:
   just --list

dev:
   cd vitepress && yarn docs:dev

publish:
   python variables.py 
   cp docs/* vitepress/docs
   cd vitepress && yarn docs:build && cd ..
   ghp-import -nfp vitepress/docs/.vitepress/dist

prettier:
   npx prettier docs --write   