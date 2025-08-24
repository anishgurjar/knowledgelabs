import { add } from './first_test';

describe('add', () => {
    it('adds two numbers', () => {
        expect(add(2, 3)).toBe(5);
    });
});

it.each([
    [0,0,0],
    [-1,1,0],
    [1.5,2.5,4]
])('works for %p + %p', (a,b,expected)=>{
    expect(add(a,b)).toBe(expected);
});
