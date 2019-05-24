open System


// let countPairs socks = 
//     let rec recCountPairs internalSocks count =
//         match internalSocks with
//         | [] -> count
//         | h::t -> recCountPairs t (count+1)
//     recCountPairs socks 0

// Cheats by using a sorted list
let countPairsSorted socks = 
    let rec recCountPairs internalSocks count =
        match internalSocks with
        | [] -> count
        | h::[] -> count
        | h::h2::t -> 
            if h = h2 then
                recCountPairs t (count+1)
            else 
                recCountPairs (h2::t) count
    recCountPairs (List.sort socks) 0

[<EntryPoint>]
let main argv =
    let numberOfSockes = Console.ReadLine() |> int
    let colors = Console.ReadLine().Split([|" "|], StringSplitOptions.RemoveEmptyEntries)       |> List.ofArray
    // printfn "%d" numberOfSockes
    // printfn "%A" colors
    printfn "%d" <| countPairsSorted colors
    0
