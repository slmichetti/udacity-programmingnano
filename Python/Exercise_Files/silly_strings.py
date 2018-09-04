import random
import words

    # Your code should choose a random
    # sentence template from the templates
    # list.
    #
    # Then it should create a string based on
    # that template, but with random nouns
    # and verbs in place of the {{noun}} and
    # {{verb}} markers in it.
    #
    # Then it should return the resulting


def silly_string(nouns, verbs, templates): 
        template = random.choice(templates) #choose a random template                       
        output = [] #create a list to append the sentences into
        length = len(templates)
        pos = 0 #to track where location in the template string

        while pos <len(template):
                if template[pos:pos+8] == '{{noun}}':
                        output.append(random.choice(nouns)) #add the random noun to the output
                        pos += 8
                elif template[pos:pos+8] == '{{verb}}':
                        output.append(random.choice(verbs)) #add the random verb to the output list
                        pos += 8
                else:
                        output.append(template[pos]) #add a character to the output
                        pos += 1

        output = ''.join(output)

        return output


if __name__ == '__main__':
    print(silly_string(words.nouns, words.verbs,
                       words.templates))
