import luigi
import requests

class URLResponse(luigi.Task):
    url = luigi.Parameter()

    def run(self):
        with self.output().open('w') as out_file:
            req = requests.get(self.url)
            result = req.content
            out_file.write(self.url + ':\n' + str(result) + '\n\n')

    def output(self):
        return luigi.LocalTarget('luigi-{0}.txt'.format(self.url.split('/')[-1]))

class AggregateResults(luigi.Task):
    num_links = luigi.IntParameter(default=1)

    @property
    def urls(self):
        return ['https://httpbin.org/delay/{0}'.format(i) for i in range(1, self.num_links)]

    def requires(self):
        return [URLResponse(url) for url in self.urls]

    def run(self):
        with input.open('r') as in_file, self.output().open('w') as out_file:
            for input in self.input():
                out_file.write('\n'.join(in_file.readlines()))

    def output(self):
        return luigi.LocalTarget('luigi-output.txt')

if __name__ == '__main__':
    luigi.run()

# with open('test.txt', 'w') as out_file:
#     with open('luigi_output.txt', 'r') as in_file:
#         out_file.write(in_file.readlines() + '\n\n')
