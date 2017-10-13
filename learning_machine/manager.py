import threading

from learning_machine.models import Page


class Manager:

    __lock = threading.Lock()
    __page_dict = {
        'NaiveBayes': Page('NaiveBayes', 'Naive Bayes', 'naive_bayes/naive_bayes_body.html')
    }

    @classmethod
    def get_page(cls, page_name):

        with cls.__lock:

            try:
                return Page.objects.get(id=page_name)
            except Page.DoesNotExist as exception:

                try:
                    return cls.__page_dict[page_name].save()
                except KeyError:
                    raise exception
