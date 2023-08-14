#!/usr/bin/env node
numArguments = process.argv.length - 2

if (numArguments < 1){
    console.log("No argument")
}
else if (numArguments === 1){
    console.log("Argument found")
}
else {
    console.log("Arguments found")
}