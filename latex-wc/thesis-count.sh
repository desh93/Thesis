#!/bin/bash

function count {
    # local lwc="/Users/Stuart/latex-wc/latexcount.pl"
    # local parts=$(find /Users/Stuart/writing/thesis/parts/ -type f -name "*.tex")

    local word_count=$(perl /Users/Deshan/Documents/PhD/thesis/Thesis/latex-wc/latexcount.pl \
	/Users/Deshan/Documents/PhD/thesis/Thesis/chapters/*.tex)

    # local word_count=$(/opt/local/bin/perl ${lwc} ${parts})
    local time_since_epoch=$(date +%s)
    local db="/Users/Deshan/Documents/PhD/thesis/Thesis/latex-wc/timestamped_wordcounts.txt"

    echo "${time_since_epoch} ${word_count}" >> "${db}"
}


function count_figures {
    local figures=/Users/Deshan/Documents/PhD/thesis/Thesis/figures
    local figure_count=$(find "${figures}" -name "*.pdf" -o -name "*.png" -o -name "*.jpeg" -o -name "*.svg" | wc -l)
    local time_since_epoch=$(date +%s)
    local db="/Users/Deshan/Documents/PhD/thesis/Thesis/latex-wc/timestamped_figurecounts.txt"

    echo "${time_since_epoch} ${figure_count}" >> "${db}"
}

count
count_figures

