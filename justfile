list:
   just --list

publish: 
   cd vitepress && yarn docs:build && cd ..
   ghp-import -nfp vitepress/docs/.vitepress/dist

prettier:
   npx prettier docs --write   