type row = 32;;


let sierpinksi_triangles number =



  let () =
    let number = read_int() in
    let answer = sierpinksi_triangles number in
    List.iter (fun row -> (print_endline (String.concat " " (List.map (fun element -> string_of_int element ) row)))) answer