from typing import Any, List, Optional

def make_table(rows: List[List[Any]], labels: Optional[List[Any]] = None, centered: bool = False) -> str:
    """
    :param rows: 2D list containing objects that have a single-line representation (via `str`).
    All rows must be of the same length.
    :param labels: List containing the column labels. If present, the length must equal to that of each row.
    :param centered: If the items should be aligned to the center, else they are left aligned.
    :return: A table representing the rows passed in.
    """
    have_labels = False
    if labels:
        table = [labels] + rows[:]
        have_labels = True
    else:
        table = rows

    table = format_words(table, centered)
    bounds = ['─'*len(v) for v in table[0]]

    if have_labels:
        s =  '┌' + '┬'.join(bounds)   + '┐\n'
        s += '│' + '|'.join(table[0]) + '│\n'
        s += '├' + '┼'.join(bounds)   + '┤\n'
        table.pop(0)
    else:
        s = '┌' + '┬'.join(bounds)    + '┐\n'
    
    for ar in table:
        s += '│' + '│'.join(ar) + '│\n'
    
    s += '└' + '┴'.join(bounds) + '┘\n'

    return s
    

def format_words(table: List[List[Any]], centered:bool = False):
    """
    :param table: The table to be processed.
    :param centered: If True the contents will be centered.
    Format words so that ['123', '123456'] will become ['123   ', '123456'] or 
    [' 123  ', '123456'] if centered is True.
    :return: an 2D-list with the processed words.
    """
    for i in range (len(table[0])):
        col = [str(row[i]) for row in table]
        
        longest_len = max( [len(v) for v in col] )

        for j in range(len(col)):
            if centered:
                table[j][i] = f' {col[j]:^{longest_len}} '
            else:
                #table[j][i] = ' ' + col[j] + ' ' * (longest_len - len(col[j])) + ' '
                table[j][i] = f' {col[j]:<{longest_len}} '
    
    return table


# table = make_table(
#     rows=[
#         ["Lemon", 18_3285, "Owner"],
#         ["Sebastiaan", 18_3285.1, "Owner"],
#         ["KutieKatj", 15_000, "Admin"],
#         ["Jake", "MoreThanU", "Helper"],
#         ["Joe", -12, "Idk Tbh"]
#     ],
#     labels=["User", "Messages", "Role"],
#     centered=True
# )
# print(table)
