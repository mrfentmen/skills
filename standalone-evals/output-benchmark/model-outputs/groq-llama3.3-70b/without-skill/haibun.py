import sys

def count_errors(log):
    error_count = 0
    for line in log:
        if 'ERROR' in line:
            error_count += 1
    return error_count

log = sys.stdin.readlines()
error_count = count_errors(log)

print("As we delve into the depths of the log, a narrative unfolds, a tale of trials and tribulations, of code that faltered and failed. The errors, like whispers in the dark, hint at the struggles of the programmer, the long hours and the sleepless nights. And yet, amidst the chaos, a glimmer of hope emerges, a chance to learn and to grow, to rise above the mistakes and to forge a new path forward.")
print("The count of errors, a stark reminder of the journey, stands at", error_count)
print("In the silence, errors whisper low,")
print("A count of", error_count, "lines that did not go,")
print("As code and dreams in darkness grow.")
