import csv


class Item:
    all = []

    def __init__(self, Index, Organization, Name, Website, Country, Description, Founded, Industry, Employees):
        self.Index = Index
        self.Organization = Organization
        self.Name = Name
        self.Website = Website
        self.Country = Country
        self.Description = Description
        self.Founded = Founded
        self.Industry = Industry
        self.Employees = Employees

        Item.all.append(self)

    @classmethod
    def intance_from_csv(cls):
        with open('organizations-1000.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                Index=item.get('Index'),
                Organization=item.get('Organization'),
                Name=item.get('Name'),
                Website=item.get('Website'),
                Country=item.get('Country'),
                Description=item.get('Description'),
                Founded=item.get('Fonded'),
                Industry=item.get('Industry'),
                Employees=int(item.get('Employees')),
            )

    @classmethod
    def dict_num_employee(self):
        for i in Item.all:
            dict_n_employee.update({i.Organization: i.Employees})

    @classmethod
    def num_max_employee(self):
        key_list = list(dict_n_employee.keys())
        value_list = list(dict_n_employee.values())
        max_dict = {key_list[value_list.index(max(value_list))]: max(value_list)}
        return max_dict

    @classmethod
    def sum_all(self):
        value_list = list(dict_n_employee.values())
        return sum(value_list)

    @classmethod
    def num_industry(self):
        key_list = list(dict_n_employee.keys())
        return len(key_list)
    
    def __repr__(self):
        return f'Item({self.Index}, {self.Organization}, {self.Name}, {self.Website}, {self.Country}, {self.Founded}, {self.Description}, {self.Industry}, {self.Employees})'

    @classmethod
    def getting_uniques_industry(cls):
        industry_set = set()
        for i in Item.all:
            industry_set.add(i.Industry)
        unique_industry = list(industry_set)
        return unique_industry



Item.intance_from_csv()
dict_n_employee = {}
Item.dict_num_employee()
print(Item.all)
print(Item.num_max_employee())
print(Item.sum_all())
print(Item.num_industry())
print(len(Item.getting_uniques_industry()))
