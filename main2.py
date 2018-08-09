labels=["Positive["+str(positive)+"%]","Mixed Views["+str(mixed)+"%]","Negative["+str(negative)+"%]"]
sizes=[positive,mixed,negative]
colors=["pink","lightgreen","lightblue"]
patches,texts=plt.pie(sizes,colors=colors,startangle=90)
plt.legend(patches,labels,loc="best")
plt.title("People are reacting on"+searchTerm)
plt.axis("equal")
plt.tight_layout()
plt.show()

#PlottingThePieChart
