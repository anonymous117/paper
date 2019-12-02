if __name__ == "__main__":
    f = open("connectivity_update.txt", "r")
    values = []
    ps = []
    for x in f:
        line = x
        line2 = x
        pos = line.find("value")
        pos += 7
        line = line[pos:]
        line = line.replace("}","")
        value = float(line)
        values.append(value)
        pos2 = line2.find("\"p\":")
        pos2 += 4
        line2 = line2[pos2:]
        pos2 = line2.find(",")
        line2 = line2[:pos2]
        p = int(line2)
        ps.append(p)
    f.close()
    total_cost = 0
    for i in range(len(values)):
        point_cost = ps[i] * values[i]
        #print("cost:",point_cost)
        total_cost += point_cost
    print("total cost:",total_cost)


    #print(values)
    #print(ps)