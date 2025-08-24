const formatUser = (firstName: string, lastName?:string, age?:number):void => {
    console.log(`${firstName} ${lastName} (${age})`)
}

formatUser("anish", "gurjar")