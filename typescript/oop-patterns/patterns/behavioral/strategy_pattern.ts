/*
Design a TextFormatter system that formats text differently depending on the chosen strategy:

UpperCaseStrategy → converts all text to uppercase.

LowerCaseStrategy → converts all text to lowercase.

TitleCaseStrategy → capitalizes the first letter of each word.
*/

interface Strategy{
    apply(text:string):string;
}

class UpperCaseStrategy implements Strategy{
    apply(text: string): string {
        return text.toUpperCase()
    }
}

/*
class LowerCaseStrategy implements Strategy{
    apply(text: string): string {
        return text.toLowerCase()
    }
}

class TitleCaseStrategy implements Strategy{
    apply(text: string): string {
        return text.toLocaleUpperCase()
    }
}

*/


interface TextFormatter{
    strategy: Strategy, 
    text: string,
    format():string
}

class TextFormatter implements TextFormatter{
    text:string;

    constructor(text:string){
        this.text = text;
    }
    
    format(){
        return this.strategy.apply(this.text)
    }

    setStrategy = (strategy:Strategy):void => {this.strategy = strategy};

}

const myText = "hi, my name is Anish";

const myformatter = new TextFormatter(myText);
const mystrategy = new UpperCaseStrategy();

myformatter.setStrategy(mystrategy)

console.log(myformatter.format())

