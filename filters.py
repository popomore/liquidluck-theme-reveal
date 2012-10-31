def reveal(content):
    result = ''
    arr = content.split('<hr/>')
    for c in arr:
        result += '<div class="slides"><section>'
        result += c
        result += '</section></div>'
    return result
