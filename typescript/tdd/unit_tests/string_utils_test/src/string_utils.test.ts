import { capitalize, reverse } from "./string_utils"; 

describe("string utils", () => {
   
    test('it capitalizes', () => {
        [
            ["anish", "ANISH"],
            ["",""],
            ["123","123"]
        ].forEach(([i, o]) => {
            expect(capitalize(i as string)).toBe(o);
        })
    })

    test('reverse', () => {
        [
            ["anish", "hsina"],
            ["",""],
            ["123","321"]
        ].forEach(([i, o]) => {
            expect(reverse(i as string)).toBe(o);
        })
    })
});