class Company(object):
    def __init__(self, cid, name, carname):
        self.cid = cid
        self.name = name
        self.carname = carname

    def __str__(self):
        return "cid - %d, name - %s, carname - %s" % (self.cid, self.name, self.carname)


class Companies(object):
    def __init__(self, companies=[], last=1):
        self.companies = companies
        self.last = last

    def __getitem__(self, cid):
        for company in self.companies:
            if company.cid == cid:
                return company
        raise Exception("Product with pid={} doesn't exist!".format(cid))

    def add(self, company):
        self.companies.append(company)
        self.last += 1

    def delete(self, cid):
        ind = -1
        for index, company in enumerate(self.companies):
            if company.cid == cid:
                ind = index
            if ind > -1:
                self.companies.pop(ind)

    def exist(self, cid):
        for company in self.companies:
            if cid == company.cid:
                return True
        return False

    def empty(self):
        return not self.companies

    def find(self, m):
        if not m:
            print 'NO COMPANY PRODUCE CAR WITH SUCH SIZE '
        else:
            for company in self.companies:
                if m == company.carname:
                    print 'Such company produce cars with such size:'
                    print company.name
                    break
                else:
                    print 'No companies with such car'
                    break

    def __str__(self):
        return '\n'.join(str(company) for company in self.companies)
