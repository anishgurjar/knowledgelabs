

- Install tsc compiler using `npm install -g typescript` Typescript is statically typed langauge. 


- The official compiler of typescript is `tsc`. All typescript code end of the day compiles to js code. browser needs js, it doesn't understand ts. 

    Compiling code: 

    - option A: say I have `hello.ts` file. I can do tsc hello.ts which would convert hello.ts to hello.js and then I have to run node hello.js

    - option B: run typescript code directly using ts-node. Install `ts-node` using `npm install -g ts-node` and then run ts-node hello.ts 
    basically what ts-node is is that instead of having me to compile a ts file, have that live all in disk as js files and then running the whole thing as node, which can
    be time consuming, ts-node basically compiles to js in-memory and runs it for you directly as one command as opposed to doing the full cycle. 

    - prefer option B for development, but in prod, when CI/CD builds the code, it is always most certainly compiled to js files on disk wherever target code is running. 

- Initialize a typescript project using  `npx tsc --init` . This will give us a `tsconfig.json` file. This tsconfig.json file has all the info on how to compile code, 
where will compiled files live, etc. almost like a typescript settings file. 

- PATTERN: use package.json for running easy scripts. For quick compile / running code - we can bascially use `ts-node src/index.ts` basically suggesting - quick compile, don't write to disk, and main entry point of ts code app is `index.ts` inside `src` folder. But for building you do `tsc`, which means it will look at entry folder based on the 
tsconfig file, see that it's src, and then compile everything. this will be on disk. 
    ```
        {
        "scripts": {
            "start": "ts-node src/index.ts",
            "build": "tsc"
            }
        }
    ```
    and then run the code using npm start. 
