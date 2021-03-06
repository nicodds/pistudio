# Copyright 2018 Domenico Delle Side <nico@delleside.org>
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing,
#    software distributed under the License is distributed on an "AS
#    IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either
#    express or implied.  See the License for the specific language
#    governing permissions and limitations under the License.

class AbstractSensor(object):
    
    def __init__(self, name='sensor', debug=False):
        self._name    = name
        self._debug   = debug


    def convert(self, measure):
        print("""%s --- This method currently only return the value
        passed. You should reimplement it in your specialized class.""" %(self._name))

        return measure

    def measure(self):
        print("""%s --- This method currently only return the 0.0. 
        You should reimplement it in your specialized class.""" %(self._name))

        return 0.0
    

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

