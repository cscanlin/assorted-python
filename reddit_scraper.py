import praw

def is_code_format(line):
    split_line = line.split(' ')
    for char in split_line[:4]:
        if char != '':
            return False
    else:
        return True


def is_import_statement(line):
    split_line = line.split(' ')
    if 'import' in split_line:
        import_index = split_line.index('import')
        if split_line[import_index+1] == '':
            return False
        for word in split_line[import_index+2:]:
            if len(word) > 0:
                return False

        return True

    else:
        return False


def check_submission_for_bad_import(submission):
    bad_lines = []
    for i, line in enumerate(submission.selftext.split('\n')):
        if is_import_statement(line) and not is_code_format(line):
            print 'LINE {0} CONTAINS BAD IMPORT STATEMENT: {1}\n'.format(i, line)
            bad_lines.append(i)
    return bad_lines


if __name__ == '__main__':
    r = praw.Reddit('Comment Scraper 1.0 '
                     'https://praw.readthedocs.org/en/latest/'
                     'pages/comment_parsing.html')
    submission = r.get_submission(submission_id='3p8x7x')
    bad_lines = check_submission_for_bad_import(submission)
    print bad_lines
