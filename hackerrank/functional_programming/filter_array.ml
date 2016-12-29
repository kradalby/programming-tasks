let rec read_lines () =
  try let line = read_line () in
    int_of_string (line) :: read_lines()
  with
    End_of_file -> []


let f n arr = 
  List.filter (fun number -> number < n) arr



let () = 
  let n::arr = read_lines() in
  let ans = f n arr in
  List.iter (fun x -> print_int x; print_newline ()) ans;;