export interface Itool<I, O> {
    execute(input: I): O;
}