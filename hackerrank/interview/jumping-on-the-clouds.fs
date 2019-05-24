//Enter your code here. Read input from STDIN. Print output to STDOUT
open System

let findOptimalPath clouds =
    let rec recFindOptimalPath internalClouds counter =
        match internalClouds with
        | [] -> counter
        | h::[] -> counter
        | h::h2::h3::t -> 
            if h3 = 0 then
                recFindOptimalPath (h3::t) (counter+1)
            else
                recFindOptimalPath (h2::h3::t) (counter+1)
        | h::h2::t -> recFindOptimalPath (h2::t) (counter+1)
    recFindOptimalPath clouds 0

[<EntryPoint>]
let main argv =
    let numberOfClouds = Console.ReadLine() |> int
    let clouds = Console.ReadLine().Split([|" "|], StringSplitOptions.RemoveEmptyEntries)
        |> List.ofArray 
        |> List.map int

    printfn "%d" <| findOptimalPath clouds
    0
