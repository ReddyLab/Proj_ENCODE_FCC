fun_cut = function(vec_num_input, num_prob = 0.25){
    ### setup quantiles and labels
    vec_num_probs  = seq(0, 1, by = num_prob)
    vec_num_quans  = quantile(vec_num_input, probs = vec_num_probs)
    vec_txt_label  = paste0("Q", seq(1, length(vec_num_probs)-1))
    
    ###
    vec_num_output = cut(
        vec_num_input, 
        breaks = vec_num_quans, 
        labels = vec_txt_label,
        include.lowest=TRUE
    )
    return(vec_num_output)
}

fun_display_table = function(dat) {
    dat |> 
        kableExtra::kable("html") |> 
        kableExtra::kable_styling("striped") %>% 
        kableExtra::scroll_box(width = "100%") %>%
        as.character() %>%
        IRdisplay::display_html()    
}