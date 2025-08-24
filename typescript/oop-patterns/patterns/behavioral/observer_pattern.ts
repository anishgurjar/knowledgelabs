interface RateObserver{    
    update(rate:number):void
}

class MortgageRateFeed{

    private rate:number;
    private observers: RateObserver[];

    constructor(){
        this.observers = [];
        this.rate = 0;
    }

    addObserver(observer: RateObserver){
        this.observers.push(observer);
    }

    setRate(rate:number):void{
        this.rate = rate;
        this.observers.forEach(observer => observer.update(rate));
    }

    getRate():void{
        console.log(this.rate);
    }
}

class PricingEngine implements RateObserver{
    private rate: number = 0;

    update(rate: number): void {
        this.rate = rate;
    }
    calculatePrice():void{
        //some calculations.
        console.log(`Did calculations with rate: ${this.rate}`)
    }
}


class CompanyRateNotifier implements RateObserver{
    private rate: number = 0;

    update(rate: number): void {
        this.rate = rate;
    }
    showRate():void{
        //some UI stuff.
        console.log(`Hey everyone, the new rate is: ${this.rate}`)
    }
}

class AnalyticsRateNotifer implements RateObserver{
    private rate: number = 0;

    update(rate: number): void {
        this.rate = rate;
    }
    showRate():void{
        //some analytics stuff stuff.
        console.log(`Hey analytics engine, the new rate is: ${this.rate}`)
    }
}


const myRateFeed = new MortgageRateFeed();
const myCompanyRateNotifier = new CompanyRateNotifier();
const myPricingEngine = new PricingEngine();
const myAnalyticsRateNotifier = new AnalyticsRateNotifer();
myRateFeed.addObserver(myCompanyRateNotifier)
myRateFeed.addObserver(myPricingEngine)
myRateFeed.addObserver(myAnalyticsRateNotifier)

myRateFeed.setRate(0.5);

myCompanyRateNotifier.showRate();




