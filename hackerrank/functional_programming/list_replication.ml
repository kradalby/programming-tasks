let rec read_lines () =
  try let line = read_line () in
    int_of_string (line) :: read_lines()
  with
    End_of_file -> []

let rec replicate amount number acc =
  match amount with
  | 0 -> acc
  | n -> replicate (n-1) number acc@[number]

let f n arr = 
  List.flatten (List.map (fun number -> replicate n number [] ) arr)


let () =
  let n::arr = read_lines() in
  let ans = f n arr in
  List.iter (fun x -> print_int x; print_newline ()) ans;;