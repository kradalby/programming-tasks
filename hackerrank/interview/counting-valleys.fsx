open System

let countValleys steps =
    let rec recCountValleys internalSteps level valleys =
        match internalSteps with
        | [] -> valleys
        | 'U'::t -> recCountValleys t (level+1) (if level = -1 then valleys+1 else valleys)
        | 'D'::t -> recCountValleys t (level-1) valleys
        | h::t -> recCountValleys t level valleys
    recCountValleys steps 0 0


let steps = Console.ReadLine() |> Seq.toList

printfn "%d" <| countValleys steps
    

