open System

let findOccurences char s n =
    let rec baseOccurences char s count =
        match s with
        | [] -> count
        | h::t -> 
            if h = char then 
                baseOccurences char t count+1L
            else
                baseOccurences char t count
    let l = List.length s |> int64
    let baseCharCount = baseOccurences char s 0L
    let baseCount = floor((float n) / (float l))
    let reminder = n % l |> int
    let reminderCharCount = 
        // This whole check is done because .[] slice notation is _inclusive_
        if reminder = 0 then 
            0L 
        else 
            baseOccurences char (s.[..reminder-1]) 0L

    (baseCharCount * (int64 baseCount)) + reminderCharCount

[<EntryPoint>]
let main argv =
    let s = Console.ReadLine() |> Seq.toList
    let n = Console.ReadLine() |> int64

    printf "%d" <| findOccurences 'a' s n
    0
